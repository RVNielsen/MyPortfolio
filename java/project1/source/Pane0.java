package code;

import javafx.scene.layout.GridPane;
import javafx.scene.text.*;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;


public class Pane0
{
      private boolean haveGuessed;
      private Text t = new Text("What is your favorite color?");
      private TextField tF = new TextField();
      private Button b = new Button("Check");
      private Text t2 = new Text("");

      // page 0 main function
      // favorite color
      protected String pane0Main(CenterPane cP, Button lB)
      {
            haveGuessed = false;
            cP.add(t, 0, 0);
            cP.add(tF, 0, 1);
            cP.add(b, 0, 2);
            cP.add(t2, 0, 3);
            b.setOnAction(ae->
            {
                  check(lB);
            });
            return "Blue";
      }

      public void check(Button leftButton)
      {
            if(haveGuessed == true)
            {
                  t2.setText("correct :)");
                  leftButton.setVisible(true); // ***Button1 visible***
            }
            else
            {
                  haveGuessed = true;
                  t2.setText("WRONGGGGGGG!!!!!");
            }
      }
}
