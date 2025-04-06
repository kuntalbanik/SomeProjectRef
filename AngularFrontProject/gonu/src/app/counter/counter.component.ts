import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  imports: [],
  templateUrl: './counter.component.html',
  styleUrl: './counter.component.scss',
})
export class CounterComponent {
  counter: number = 0;

  // click counter functionality
  btnEventHandle(param: string) {
    if (param == 'dec') {
      // condition to check counter if zero
      if (this.counter > 0) {
        this.counter -= 1;
      }
    } else if (param == 'inc') {
      this.counter += 1;
    } else {
      this.counter = 0;
    }
  }

  // Event Handler
  handleEvent(event: MouseEvent) {
    console.log('Event : ', event.type);
    console.log('Event target : ', event.target);
    console.log('Class Name : ', (event.target as Element).className);
  }

  handleEvent2(event: MouseEvent) {
    console.log('MouseEnter : ', event.type);
  }
  handleEvent3(event: Event) {
    console.log('Input Event : ', event.type);
    // console.log('Value : ', (event.target as HTMLInputElement).value);
  }

  // 
  // 
  // 
  // Get and set value
  // 
  // 
  name = "";
  inputStorage(user: Event) {
    // this.name = user;
    // console.log(user," : ", typeof(user));
    this.name = (user.target as HTMLInputElement).value;
    // console.log(this.name);
  }
  displayName = "";
  showName(){
    this.displayName = this.name;
  }
  getMail(val: string){
    console.log(val);
    
  }
}
