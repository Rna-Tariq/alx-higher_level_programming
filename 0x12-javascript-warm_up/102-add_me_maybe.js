#!/usr/bin/node
// executes x times a function.

export function addMeMaybe (number, theFunction) {
    number++;
    theFunction(number);
}
