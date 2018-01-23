from big_data.test.api import TestApi


class Test(TestApi):
    def test(self):
        # self.request_get("/mine")
        # self.request_post("/nodes/register", data={"nodes":["http:127.0.0.1:5001"]})
        self.request_get("/nodes/resolve")