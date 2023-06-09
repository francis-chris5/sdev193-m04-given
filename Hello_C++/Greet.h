
#ifndef Greet_h
#define Greet_h

#include "iostream"

using namespace std;

namespace Greetings {

    class StandardGreeting {

        public:
          StandardGreeting(int exclaim);

        protected:
          string STANDARD_MESSAGE = "Hello World";
          string output;
          
    };

} // namespace Greetings

#endif