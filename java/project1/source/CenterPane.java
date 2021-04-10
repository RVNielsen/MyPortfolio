package code;

import javafx.application.Application;
import javafx.scene.layout.GridPane;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.event.EventHandler;
import javafx.scene.text.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;
import java.util.Scanner;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import javafx.scene.control.Button;


import code.Pane1;
import code.Pane0;

public class CenterPane extends GridPane
{
      private Pane0 p0 = new Pane0();
      private Pane1 p1 = new Pane1();

      // which pane are we dealing with
      // return the answer for the question on that pane
      public void which(CenterPane cP, int i, Button b)
      {
            switch(i)
            {
                  case 0:
                        // favorite color
                        p0.pane0Main(cP, b);
                        break;
                  case 1:
                        // horse game
                        p1.pane1Main(cP, b);
                        break;
                  default:
                        
            }
      }
}
