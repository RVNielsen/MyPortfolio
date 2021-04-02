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
      BorderPane root = new BorderPane();
      GridPane pane1 = new GridPane();
      GridPane pane2 = new GridPane();
      GridPane pane3 = new GridPane();
      GridPane pane4 = new GridPane();
      GridPane fPane = new GridPane();
      Text text1, text2, text3;
      Button aButton, bButton, button1, button2, button3;
      Scene scene;
      Stage stage;
      TextField tField1, tField2;
      String str1, str2;
      String ans1, ans2;

      @Override
      public void start(Stage stage)
      {
            fPane = leftSide();
            pane4 = centerPage();
            setup();
            Scene scene = new Scene(root, 700, 600);
            stage.setTitle("BorderPaneDemo");
            stage.setScene(scene);
            stage.show();
      }

      public void setup()
      {
            root.setStyle("-fx-background-color: GRAY");
            root.setTop(new CustomPane("Top"));
            root.setRight(new CustomPane("Right"));
            root.setBottom(new CustomPane("Bottom"));
            root.setLeft(fPane);
            root.setCenter(pane4);
      }

      class CustomPane extends StackPane
      {
            public CustomPane(String title)
            {
                  getChildren().add(new Label(title));
                  setStyle("-fx-border-color: GREEN");
                  setPadding(new Insets(11.5, 12.5, 13.5, 14.5));
            }
      }
      
      public GridPane leftSide()
      {
            button1 = new Button("Button 1");
            button2 = new Button("Button 2");
            button3 = new Button("Button 3");

            fPane.add(button1, 0, 0);
            fPane.add(button2, 0, 1);
            fPane.add(button3, 0, 2);

            button1.setOnAction(ae->
            {
                  pane4.getChildren().clear();
                  pane4.getChildren().add(pane1);
            });
            button2.setOnAction(ae->
            {
                  pane4.getChildren().clear();
                  pane4.getChildren().add(pane2);
            });
            button3.setOnAction(ae->
            {
                  pane4.getChildren().clear();
                  pane4.getChildren().add(pane3);
            });

            button2.setVisible(false);
            button3.setVisible(false);

            return fPane;
      }

      public GridPane centerPage()
      {
            ans1 = new String("hi");
            ans2 = new String("hello");
            aButton = new Button("aButton");
            bButton = new Button("bButton");
            tField1 = new TextField("");
            tField2 = new TextField("");
            tField1.setFont(Font.font("Courier New", FontWeight.BOLD, FontPosture.REGULAR, 50));
            tField2.setFont(Font.font("Courier New", FontWeight.BOLD, FontPosture.REGULAR, 50));
            text1 = new Text("This is pane 1");
            text2 = new Text("This is pane 2");
            text3 = new Text("This is pane 3");
            
            pane1.add(text1, 0, 0);
            pane1.add(aButton, 0, 1);
            pane1.add(tField1, 0, 2);

            pane2.add(text2, 0, 0);
            pane2.add(bButton, 0, 1);
            pane2.add(tField2, 0, 2);

            pane3.add(text3, 0, 0);

            pane4.add(pane1, 0, 0);

            pane1.relocate(10, 50);
            pane2.relocate(10, 50);
            pane3.relocate(10, 50);
            pane4.relocate(10, 100);

            aButton.setOnAction(ae->
            {
                  str1 = new String(tField1.getText());
                  if(str1.equals(ans1))
                  {
                        button2.setVisible(true);
                  }
            });
            bButton.setOnAction(ae->
            {
                  str2 = new String(tField2.getText());
                  if(str2.equals(ans2))
                  {
                        button3.setVisible(true);
                  }
            });

            return pane4;
      }
}