// TODO: define the 'ranks' constant
let ranks = 1...8
// TODO: define the 'files' constant
let files = "A"..."H"


func isValidSquare(rank: Int, file: String) -> Bool {
  if ranks.contains(rank) && files.contains(file){
    return true 
  } 
  else {
        return false
  }
}

func getRow(_ board : [String], rank: Int) -> [String] {
  
  return Array(board[(rank-1)*8..<(rank*8)])
}
