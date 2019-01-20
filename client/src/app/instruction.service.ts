import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { ErrorMessage } from './messages-container.service';


export interface Position {
  x: number;
  y: number;
}

export enum Direction {
  NORTH = 'NORTH',
  WEST = 'WEST',
  SOUTH = 'SOUTH',
  EAST = 'EAST'
}

export interface RobotConfiguration {
  position: Position;
  direction: Direction;
  errors: Array<ErrorMessage>;
  output: string
}

@Injectable({
  providedIn: 'root'
})
export class InstructionService {

  constructor(private http: HttpClient) { }
  sendInstructions(instructions: string): Observable<RobotConfiguration> {
    return this.http.post<RobotConfiguration>('http://localhost:6543/', {instructions:instructions});
  }
  reset(){
    return this.http.get('http://localhost:6543/reset');
  }
}
