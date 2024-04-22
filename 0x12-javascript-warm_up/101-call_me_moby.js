#!/usr/bin/node
// executes x times a function.

export function callMeMoby (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}
