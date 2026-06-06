func totalBirdCount(_ birdsPerDay: [Int]) -> Int {
  var sum = 0
  for a in birdsPerDay{
    sum+=a
  }
  return sum
}

func birdsInWeek(_ birdsPerDay: [Int], weekNumber: Int) -> Int {
  var sum = 0
  for i in (weekNumber-1)*7..<(weekNumber)*7 {
    sum+=birdsPerDay[i]
  }
  return sum
}

func fixBirdCountLog(_ birdsPerDay: [Int]) -> [Int] {
  var b = birdsPerDay
  for i in stride(from: 0, to: b.count, by:2) {
    b[i]+=1
  }
  return b
}
