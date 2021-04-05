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

import javafx.scene.layout.HBox;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;


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

      Pane root2 = new Pane();

      GridPane lPane = new GridPane();
      GridPane qPane = new GridPane();

      Scene scene;
      Stage stage;

      Label hL;
      HBox h;
      Stage stage2;

      Image map;
      ImageView mapView;

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

            stage2 = new Stage();
            hL = new Label("Other window");
            h = new HBox(hL);
            h.setPrefWidth(400);
            h.setPrefHeight(300);
            stage2.setScene(new Scene(h));
            stage2.show();

            map = new Image("images/map.jpg");
            mapView = new ImageView(map);
            root2.getChildren().addAll(mapView);
            mapView.setFitWidth(420);
            mapView.setFitHeight(240);
            h.setStyle("-fx-background-color: GREEN");
            h.getChildren().addAll(root2);
      }

      // configure the root pane
      public void setup()
      {
            // root.setStyle("
            //       -fx-alignment: center;
            //       -fx-background-color: GRAY;
            //       -fx-font: 30 Verdana;
            //       ");
            root.setStyle("-fx-alignment: center");
            root.setStyle("-fx-background-color: GRAY");
            root.setStyle("-fx-font: 30 Verdana");
            // root.setStyle("-fx-font-family: Courier New");
            root.setTop(new CustomPane("Welcome to this Game!\n"));
            root.setBottom(new CustomPane("(It is a game)"));
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
                  hL.setText("First button");
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
