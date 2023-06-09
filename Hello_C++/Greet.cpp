
#include "Greet.h"

using namespace Greetings;



StandardGreeting::StandardGreeting(int exclaim) {

    output = STANDARD_MESSAGE;
    for (int i = 0; i < exclaim; i++) {
        output += "!";
    }

} // end constructor



void StandardGreeting::SayHi() { 

    cout << output; 
    
} //end SayHi()


