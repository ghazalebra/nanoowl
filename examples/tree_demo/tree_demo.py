(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples$ cd tree_demo
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples/tree_demo$ ls
index.html  tree_demo.py
(nanoowlenv) ghebr@tegra-ubuntu:~/Desktop/nanoowl/examples/tree_demo$ vim tree_demo.py































































        await ws.prepare(request)

        logging.info("Websocket connected.")

        request.app['websockets'].add(ws)

        try:
            async for msg in ws:
                logging.info(f"Received message from websocket.")
                if "prompt" in msg.data:
                    header, prompt = msg.data.split(":")
                    logging.info("Received prompt: " + prompt)
                    try:
                        tree = Tree.from_prompt(prompt)
                        clip_encodings = predictor.encode_clip_text(tree)
                        owl_encodings = predictor.encode_owl_text(tree)
                        prompt_data = {
                            "tree": tree,
                            "clip_encodings": clip_encodings,
                            "owl_encodings": owl_encodings
                        }
                        logging.info("Set prompt: " + prompt)
                    except Exception as e:
                        print(e)
        finally:
            request.app['websockets'].discard(ws)

        return ws


    async def on_shutdown(app: web.Application):
        for ws in set(app['websockets']):
            await ws.close(code=WSCloseCode.GOING_AWAY,
                        message='Server shutdown')


    async def detection_loop(app: web.Application):

        loop = asyncio.get_running_loop()

        logging.info("Opening camera.")
        if CAMERA_URL:
            camera = cv2.VideoCapture(CAMERA_URL)
        else:
            camera = cv2.VideoCapture(CAMERA_DEVICE)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        logging.info("Loading predictor.")

        def _read_and_encode_image():

            re, image = camera.read()

            if not re:
                return re, None

            image_pil = cv2_to_pil(image)

            if prompt_data is not None:
                prompt_data_local = prompt_data
                t0 = time.perf_counter_ns()
                detections = predictor.predict(
                    image_pil,
                    tree=prompt_data_local['tree'],
                    clip_text_encodings=prompt_data_local['clip_encodings'],