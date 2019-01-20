import { Component, OnInit, Input } from '@angular/core';
import { Robot } from '../robot/robot.component';
import { MessagesContainerService, TypedMessage } from '../messages-container.service';

@Component({
  selector: 'messages',
  templateUrl: './messages.component.pug',
  styleUrls: ['./messages.component.scss']
})
export class MessagesComponent implements OnInit {
  @Input() robot: Robot
  constructor(public messagesContainerService: MessagesContainerService) { }

  ngOnInit() {
  }

  display(e:TypedMessage):string{
    if(e.text === 'ignored'){
      return `Unknown instruction "${e.instruction}" has been ignored.`;
    }
    else if(e.text==='bad_param_amount'){
      return `Instruction "${e.instruction}" called with wrong parameters amount.`;
    }
    else if(e.text==='bad_param_type'){
      return `Instruction "${e.instruction}" called with wrong parameters type.`;
    }
    else if(e.instruction==='REPORT'){
      return e.text;
    }
    return `Instruction ${e.instruction} ignored due to : "${e.text}"`
  }
}
