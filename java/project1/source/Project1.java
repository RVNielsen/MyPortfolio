package code;

import javafx.scene.shape.Circle;
import java.util.Scanner;
import java.io.File;
import java.io.InputStream;

import javafx.scene.layout.Pane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.FlowPane;

import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.application.Application;
import javafx.scene.text.*;

import javafx.scene.paint.Color;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.text.TextAlignment;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.HPos;


public class Project1 extends Application
{
      final int NUM = 5;
      Button[] lButton = new Button[NUM];
      Button[] qButton = new Button[NUM];
      TextField[] tField = new TextField[NUM];
      String[] guess = new String[NUM];
      String[] ans = new String[NUM];
      Text[] text = new Text[NUM];

      BorderPane root = new BorderPane();
      GridPane pane0 = new GridPane();
      GridPane pane1 = new GridPane();
      GridPane pane2 = new GridPane();
      GridPane pane3 = new GridPane();
      GridPane pane4 = new GridPane();

      GridPane lPane = new GridPane();
      GridPane qPane = new GridPane();

      Scene scene;
      Stage stage;

      @Override
      public void start(Stage stage)
      {
            lPane = leftSide();
            qPane = centerPage();
            setup();

            // make a window and configure it
            Scene scene = new Scene(root, 700, 600);
            stage.setTitle("BorderPaneDemo");
            stage.setScene(scene);
            stage.show();
      }

      // configure the root pane
      public void setup()
      {
            root.setStyle("-fx-alignment: center");
            root.setStyle("-fx-background-color: GRAY");
            root.setTop(new CustomPane("Top"));
            root.setBottom(new CustomPane("Bottom"));
            root.setLeft(lPane);
            root.setCenter(qPane);
      }

      // configure each block of the root pane
      class CustomPane extends StackPane
      {
            public CustomPane(String title)
            {
                  getChildren().add(new Label(title));
                  setStyle("-fx-border-color: GREEN");
                  setPadding(new Insets(15, 15, 15, 15));
            }
      }

      // configure the buttons on the left block
      public GridPane leftSide()
      {
            for(int a = 0; a < NUM; a++)
            {
                  lButton[a] = new Button("lButton " + a);
                  lPane.add(lButton[a], 0, a);
                  if(a > 0)
                  {
                        lButton[a].setVisible(false);
                  }
            }

            lButton[0].setOnAction(ae->
            {
                  qPane.getChildren().clear();
                  qPane.getChildren().add(pane0);
            });
            lButton[1].setOnAction(ae->
            {
                  qPane.getChildren().clear();
                  qPane.getChildren().add(pane1);
            });
            lButton[2].setOnAction(ae->
            {
                  qPane.getChildren().clear();
                  qPane.getChildren().add(pane2);
            });
            lButton[3].setOnAction(ae->
            {
                  qPane.getChildren().clear();
                  qPane.getChildren().add(pane3);
            });
            lButton[4].setOnAction(ae->
            {
                  qPane.getChildren().clear();
                  qPane.getChildren().add(pane4);
            });

            return lPane;
      }

      // setup an inner pane for the center block
      public GridPane pageSetup(GridPane gPane, Integer i)
      {
            gPane.add(text[i], 0, 0);
            gPane.add(qButton[i], 0, 1);
            gPane.add(tField[i], 0, 2);
            return gPane;
      }

      // check if the user input matches the answer
      public void check(int n)
      {
            guess[n] = new String(tField[n].getText());
            if(guess[n].equals(ans[n]))
            {
                  lButton[n + 1].setVisible(true);
            }
      }

      // configure the question pane
      public GridPane centerPage()
      {
            for(int b = 0; b < 5; b++)
            {
                  ans[b] = new String("1" + b);
                  qButton[b] = new Button("qButton " + b);
                  tField[b] = new TextField();
                  tField[b].setFont(Font.font("Courier New", 50));
                  text[b] = new Text("This is pane " + b);
            }

            pane0 = pageSetup(pane0, 0);
            pane1 = pageSetup(pane1, 1);
            pane2 = pageSetup(pane2, 2);
            pane3 = pageSetup(pane3, 3);
            pane4 = pageSetup(pane4, 4);

            qButton[0].setOnAction(ae->
            {     
                  check(0);
            });
            qButton[1].setOnAction(ae->
            {     
                  check(1);
            });
            qButton[2].setOnAction(ae->
            {     
                  check(2);
            });
            qButton[3].setOnAction(ae->
            {     
                  check(3);
            });
            
            qPane.setStyle("-fx-background-color: blue");
            qPane.add(pane0, 0, 0);
            return qPane;
      }
}
