package code;

import javafx.application.Application;
import javafx.scene.layout.GridPane;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.event.EventHandler;
import javafx.scene.text.*;


public class CenterPane extends GridPane
{
      public void which(CenterPane cP, int i)
      {
            if(i == 0)
            {
                  p0Funct(cP);
            }
      }

      protected void p0Funct(CenterPane cP)
      {
            cP.add(new Text("What is your favorite color?"), 0, 0);
      }
}