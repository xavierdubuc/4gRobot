import { Component, Input, OnInit } from '@angular/core';
import { Robot } from '../robot/robot.component'

@Component({
  selector: 'app-rectenv',
  templateUrl: './rectenv.component.pug',
  styleUrls: ['./rectenv.component.scss']
})
export class RectenvComponent implements OnInit {

  @Input()
  set sizeY(sizeY: number) {
    this._sizeY = (sizeY ? sizeY : 5);
  }
  @Input()
  set sizeX(sizeX: number) {
    this._sizeX = (sizeX ? sizeX : 5);
  }
  @Input() robot: Robot;

  private _sizeX = 5;
  private _sizeY = 5;
  tiles = null;

  constructor() { }

  ngOnInit() {
    this.tiles = this._generate_tiles()
  }

  get sizeX(): number { return this._sizeX }
  get sizeY(): number { return this._sizeY }

  invert_y(y: number): number {
    return (this._sizeY - 1) - y;
  }
  robot_is_in_tile(robot: Robot, x: number, y: number): boolean {
    var on_tile = !!robot && robot.position.x === x && robot.position.y === this.invert_y(y);
    if(on_tile){
      this.tiles[this.invert_y(y)][x] = true;
    }
    return on_tile;
  }
  tile_is_empty(x: number, y: number): boolean {
    return this.tiles[this.invert_y(y)][x];
  }

  private _generate_tiles(): boolean[][] {
    var tiles = [];
    for (var i = 0; i < this._sizeY; i++) {
      tiles.push([]);
      for (var j = 0; j < this._sizeX; j++) {
        tiles[i].push(false);
      }
    }
    return tiles;
  }
}
