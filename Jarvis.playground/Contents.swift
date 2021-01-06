import UIKit

class Point {
    let x: Int
    let y: Int
    
    init(x: Int, y: Int) {
        self.x = x
        self.y = y
    }
}

// Возвращает true, если p → q → r - поворот против часовой стрелки.
// Векторное произведение
func cww(p: Point, q: Point, r: Point) -> Bool {
    let value = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    
    if value >= 0 {
        return false
    } else {
        return true
    }
}

func convexHull(points: [Point]) {
    let n = points.count
    
    // если меньше 3 точек
    guard n >= 3 else {
        return
    }
    
    var next = Array(repeating: -1, count: n)
    
    // 1. Находим самую точку
    var leftMost = 0
    
    for i in 1..<n {
        if points[i].x < points[leftMost].x {
            leftMost = i
        }
    }
    
    var p = leftMost
    var q = 0
    
    // пока p не станет левым
    repeat {
        q = (p + 1) % n
        for i in 0..<n {
            // Если поворот против часовой стрелки
            if cww(p: points[p], q: points[i], r: points[q]) {
                q = i
            }
        }
        
        next[p] = q
        p = q
    } while p != leftMost
    
    display(points: points, next: next)
}

func display(points: [Point], next: [Int]) {
    print("Точки выпуклой оболочки:")
    
    for i in 0..<next.count {
        if next[i] != -1 {
            print("(\(points[i].x), \(points[i].y))")
        }
    }
}

let points1 = [
    Point(x: 0, y: 3),
    Point(x: 4, y: 2),
    Point(x: 3, y: 5),
    Point(x: 5, y: 3),
    Point(x: 3, y: 0),
    Point(x: 1, y: 1),
    Point(x: 1, y: 2),
    Point(x: 2, y: 2)
]

print("Test1")
convexHull(points: points1)

let points2 = [
    Point(x: 0, y: 3),
    Point(x: 2, y: 3),
    Point(x: 1, y: 1),
    Point(x: 2, y: 1),
    Point(x: 3, y: 0),
    Point(x: 0, y: 0),
    Point(x: 3, y: 3)
]

print("Test2")
convexHull(points: points2)

let points3 = [
    Point(x: -25, y: 7),
    Point(x: 32, y: 11),
    Point(x: -2, y: -25),
    Point(x: 27, y: -16),
    Point(x: 53, y: 0),
    Point(x: 0, y: 0),
    Point(x: 1, y: 1)
]

print("Test3")
convexHull(points: points3)


