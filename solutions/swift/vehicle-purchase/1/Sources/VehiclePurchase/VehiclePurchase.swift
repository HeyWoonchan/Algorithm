func canIBuy(vehicle: String, price: Double, monthlyBudget: Double) -> String {
  
  let monthlyPrice = price/60.0
  if monthlyPrice <= monthlyBudget {
    return "Yes! I\'m getting a \(vehicle)"
  }
  else if monthlyPrice*90.0/100.0 <= monthlyBudget {
    return "I\'ll have to be frugal if I want a \(vehicle)"
  }
  else if monthlyPrice > monthlyBudget*10.0/100.0{
    return "Darn! No \(vehicle) for me"
  }

  return ""
}

func licenseType(numberOfWheels wheels: Int) -> String {
  if wheels == 2 || wheels == 3 {
    return "You will need a motorcycle license for your vehicle"
  }
  else if wheels == 4 || wheels == 6 {
    return "You will need an automobile license for your vehicle"
  }
  else if wheels == 18 {
    return "You will need a commercial trucking license for your vehicle"
  }
  else {
    return "We do not issue licenses for those types of vehicles"
  }
  return ""
}

func calculateResellPrice(originalPrice: Int, yearsOld: Int) -> Int {
  if yearsOld < 3 {
    return originalPrice*80/100
  }
  else if 3 <= yearsOld && yearsOld < 10 {
    return originalPrice*70/100
  }
  else {
    return originalPrice*50/100
  }
  
}
