import { TestBed } from '@angular/core/testing';

import { MessagesContainerService } from './messages-container.service';

describe('MessagesContainerService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MessagesContainerService = TestBed.get(MessagesContainerService);
    expect(service).toBeTruthy();
  });
});
