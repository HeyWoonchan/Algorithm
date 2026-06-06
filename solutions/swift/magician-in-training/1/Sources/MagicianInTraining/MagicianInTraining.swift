func getCard(at index: Int, from stack: [Int]) -> Int {
  return stack[index]
}

func setCard(at index: Int, in stack: [Int], to newCard: Int) -> [Int] {
  var stack2 = stack
  if index>=stack2.count || index < 0 {
    return stack2
  }

  stack2[index]=newCard
  return stack2
}

func insert(_ newCard: Int, atTopOf stack: [Int]) -> [Int] {
  var stack2 = stack
  stack2.append(newCard)
  return stack2
}

func removeCard(at index: Int, from stack: [Int]) -> [Int] {
  var stack2 = stack
  if index>=stack2.count || index < 0 {
    return stack2
  }

  stack2.remove(at:index)
  return stack2
}

func insert(_ newCard: Int, at index: Int, from stack: [Int]) -> [Int] {
  var stack2=stack
  if stack.count==0 && index == 0 {
    stack2.append(newCard)
    return stack2
  }
  if index>=stack2.count || index < 0 {
    return stack2
  }
  
  stack2.insert(newCard,at: index)
  return stack2
}

func checkSizeOfStack(_ stack: [Int], _ size: Int) -> Bool {
  if stack.count==size {
    return true
  }
  else {
    return false
  }
}
