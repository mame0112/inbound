import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-visit-start',
  templateUrl: './visit-start.component.html',
  styleUrls: ['./visit-start.component.css']
})
export class VisitStartComponent implements OnInit {

    isOverview = true;

    constructor() { }

    ngOnInit() {
    }

    onNextButtonClicked() {
        console.log('onNextButtonClicked');
        this.isOverview = !this.isOverview;
    }

}
