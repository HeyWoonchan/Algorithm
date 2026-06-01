// TODO: define the 'expectedMinutesInOven' constant
let expectedMinutesInOven = 40
// TODO: define the 'remainingMinutesInOven' function
func remainingMinutesInOven(elapsedMinutes a : Int) -> Int {
  return expectedMinutesInOven - a
}
// TODO: define the 'preparationTimeInMinutes' function
func preparationTimeInMinutes(layers b: Int) -> Int {
  return b*2
}
// TODO: define the 'totalTimeInMinutes' function
func totalTimeInMinutes(layers a: Int, elapsedMinutes b: Int) -> Int {
  return b+preparationTimeInMinutes(layers:a)
}