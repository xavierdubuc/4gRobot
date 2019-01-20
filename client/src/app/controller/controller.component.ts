import { Component, OnInit, Input } from '@angular/core';
import { Robot } from '../robot/robot.component'
import { InstructionService } from '../instruction.service'
import { MessagesContainerService, MessageType } from '../messages-container.service';

@Component({
  selector: 'robot-controller',
  templateUrl: './controller.component.pug',
  styleUrls: ['./controller.component.scss']
})
export class ControllerComponent implements OnInit {
  @Input() robot: Robot

  constructor(private instructionService: InstructionService,
    private messagesContainerService: MessagesContainerService) { }

  ngOnInit() { }


  execute(instruction_batch: string): void {
    var input = instruction_batch.trim();
    if (input !== '') {
      var instructions = input.split("\n");
      for (var i in instructions) {
        var instruction = instructions[i];
        this.instructionService.sendInstructions(instruction).subscribe(new_config => {
          if (!!new_config.direction) {
            this.robot.direction = new_config.direction;
          }
          if (!!new_config.position) {
            this.robot.position = new_config.position;
          }
          if (!!new_config.errors && new_config.errors.length > 0) {
            this.messagesContainerService.add_errors(new_config.errors)
          }
          if (!!new_config.output && new_config.output.length > 0) {
            this.messagesContainerService.add({
                text: new_config.output,
                instruction: 'REPORT',
                type: MessageType.INFO
            });
          }
        });
      }
    }
  }
}
