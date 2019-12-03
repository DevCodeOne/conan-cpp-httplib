#include <chrono>
#include <cstdlib>
#include <thread>

#include "httplib/httplib.h"

int main(void) {
    using namespace httplib;
    using namespace std::chrono_literals;

    Server svr;

    svr.Get("/hi", [](const Request & /*req*/, Response &res) {
        res.set_content("Hello World!", "text/plain");
    });

    std::thread stop_thread([&svr]() {
        std::this_thread::sleep_for(2s);
        svr.stop();
    });

    svr.listen("localhost", 1234);
    stop_thread.join();

    return EXIT_SUCCESS;
}
