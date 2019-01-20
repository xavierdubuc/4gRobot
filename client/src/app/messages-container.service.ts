import { Injectable } from '@angular/core';

export interface ErrorMessage {
  error: string,
  instruction: string
}

export interface TypedMessage {
  text: string,
  instruction: string,
  type: MessageType
}

export enum MessageType {
  INFO = 'info',
  ERROR = 'error'
}

@Injectable({
  providedIn: 'root'
})
export class MessagesContainerService {
  constructor() { }

  messages = Array<TypedMessage>();
  add(error: TypedMessage): void {
    this.messages.push(error);
  }
  add_errors(errors: Array<ErrorMessage>): void {
    for (var i in errors) {
      var error = errors[i];
      this.add({text:error.error, type:MessageType.ERROR, instruction: error.instruction});
    }
  }
  clear(): void {
    this.messages = [];
  }
  has_messages(): boolean {
    return !!this.messages && this.messages.length > 0;
  }
}
