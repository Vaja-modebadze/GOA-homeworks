class Rectangle {
    constructor(width, height) {
      this._width = width;
      this._height = height;
    }   
    get area() {
        return this._width * this._height;
        }
        set width(value) {
            if (value > 0) {
              this._width = value;
            } else {
              console.log("bigger than 0");
            }
          }
        }