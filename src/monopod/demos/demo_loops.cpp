#include <scenario/monopod/Joint.h>
#include <scenario/monopod/Model.h>
#include <scenario/monopod/World.h>

#include <math.h>
#include <signal.h>
#include <atomic>


/**
 * @brief This boolean is here to kill cleanly the application upon ctrl+c
 */
std::atomic_bool StopDemos(false);

/**
 * @brief This function is the callback upon a ctrl+c call from the terminal.
 *
 * @param s
 */
void my_handler(int)
{
    StopDemos = true;
}


int main(int, char**)
{
    // make sure we catch the ctrl+c signal to kill the application properly.
    struct sigaction sigIntHandler;
    sigIntHandler.sa_handler = my_handler;
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;
    sigaction(SIGINT, &sigIntHandler, NULL);
    StopDemos = false;

    scenario::monopod::World world;
    std::cout << world.name() << std::endl;

    auto monopod = world.getModel(world.modelNames()[0]);
    std::cout << monopod->name() << std::endl;

    auto jointNames = monopod->jointNames(false);
    for (std::string i: jointNames)
        std::cout << i << ", ";
    std::cout << std::endl << std::endl;

    rt_printf("loops have started \n");

    double x = 0;
    while (!StopDemos)
    {
        real_time_tools::Timer::sleep_sec(1);

        // monopod.set_torque_targets({x, x + 1});
        x++;

    }

    return 0;
}
