package code;

import java.util.Scanner;
import java.io.File;
import java.io.InputStream;

import javafx.scene.layout.Pane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.StackPane;

import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.application.Application;
import javafx.scene.text.*;

import javafx.scene.paint.Color;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;

import javafx.geometry.Insets;
import javafx.geometry.Pos;

import javafx.scene.layout.HBox;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

import code.Questions;


public class MainPanes extends Application
{
      BorderPane root = new BorderPane();
      GridPane pane0 = new GridPane();
      GridPane pane1 = new GridPane();
      GridPane pane2 = new GridPane();
      GridPane pane3 = new GridPane();
      GridPane pane4 = new GridPane();

      final int NUM = 5;
      Button[] lButton = new Button[NUM];
      Button[] qButton = new Button[NUM];
      TextField[] tField = new TextField[NUM];
      String[] guess = new String[NUM];
      String[] ans = new String[NUM];
      Text[] text = new Text[NUM];

      StackPane topPane = new StackPane();
      StackPane bottomPane = new StackPane();
      GridPane lPane = new GridPane();
      StackPane qPane = new StackPane();

      Scene scene;
      Stage stage;

      @Override
      public void start(Stage stage)
      {
            lPane = leftConfig(); // -----> to leftConfig()
            qPane = centerConfig(); // -----> to centerConfig()
            rootConfig(); // -----> to rootConfig()
            indivConfig(); // -----> to indivConfig

            // make a window and configure it
            GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
            int width = gd.getDisplayMode().getWidth();
            int height = gd.getDisplayMode().getHeight();
            Scene scene = new Scene(root, width, height);
            stage.setTitle("The Game");
            stage.setScene(scene);
            stage.show();

            // Questions q = new Questions(root2); // -----> to Questions(Pane)
      }

      // configure the buttons on the left block
      public GridPane leftConfig()
      {
            lPane.setStyle("-fx-background-color: #CCE3DE");
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
      public GridPane pageSetup(GridPane gPane, int i)
      {
            gPane.add(text[i], 0, 0);
            // text[i].setStyle("-fx-fill: #F6FFF8");
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
      public StackPane centerConfig()
      {
            for(int b = 0; b < 5; b++)
            {
                  ans[b] = new String("1" + b);
                  qButton[b] = new Button("qButton " + b);
                  tField[b] = new TextField();
                  text[b] = new Text("This is pane " + b);
            }

            pane0 = pageSetup(pane0, 0); // -----> to pageSetup(GridPane, int)
            pane1 = pageSetup(pane1, 1);
            pane2 = pageSetup(pane2, 2);
            pane3 = pageSetup(pane3, 3);
            pane4 = pageSetup(pane4, 4);

            qButton[0].setOnAction(ae->
            {     
                  check(0); // -----> to check(int)
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
            qPane.setStyle("-fx-background-color: #A4C3B2");
            qPane.getChildren().add(pane0);
            StackPane.setAlignment(pane0, Pos.CENTER);
            return qPane;
      }

      public void rootConfig()
      {
            root.setStyle("-fx-alignment: center");
            root.setStyle("-fx-font: 30 Verdana");
            root.setTop(topPane);
            root.setBottom(bottomPane);
            root.setLeft(lPane);
            root.setCenter(qPane); 
      }

      // configure the root pane
      public void indivConfig()
      {
            topPane.getChildren().addAll(new Text("Welcome to the Game!"));
            topPane.setStyle("-fx-background-color: #6B9080");
            topPane.setPadding(new Insets(15, 15, 15, 15));

            bottomPane.setStyle("-fx-background-color: #EAF4F4");
            bottomPane.getChildren().addAll(new Text("(It is a game)"));
            bottomPane.setPadding(new Insets(15, 15, 15, 15));
      }
}
