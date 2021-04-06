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

import code.CenterPane;

public class MainPanes extends Application
{
      // number of pages
      final int NUM = 5;

      // root pane
      BorderPane root = new BorderPane();
      // title pane
      StackPane topPane = new StackPane();
      // lower pane
      StackPane bottomPane = new StackPane();
      
      // buttons to control page switching
      Button[] lButton = new Button[NUM];
      GridPane lPane = new GridPane();
      
      // objects for center pages
      Button[] cButton = new Button[NUM];
      TextField[] cTField = new TextField[NUM];
      String[] cGuess = new String[NUM];
      String[] cAns = new String[NUM];
      Text cTextLower[] = new Text[NUM];
      StackPane cPane = new StackPane();
      // panes placed in the main section of the root pane
      CenterPane cPane0 = new CenterPane();
      CenterPane cPane1 = new CenterPane();
      CenterPane cPane2 = new CenterPane();
      CenterPane cPane3 = new CenterPane();
      CenterPane cPane4 = new CenterPane();

      Scene scene;
      Stage stage;

      @Override
      public void start(Stage stage)
      {
            rConfig(); // -----> to rConfig()
            lPane = lConfig(); // -----> to lConfig()
            cPane = cConfig(); // -----> to cConfig()
            tConfig(); // -----> to tConfig()
            bConfig(); // -----> to bConfig()

            cPane0.which(cPane0, 0);

            // make a window and configure it
            GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
            int width = gd.getDisplayMode().getWidth();
            width *= .9;
            int height = gd.getDisplayMode().getHeight();
            height *= .9;
            Scene scene = new Scene(root, width, height);
            stage.setTitle("The Game");
            stage.setScene(scene);
            stage.show();
      }

      public void lSetButtons(int i, CenterPane cP)
      {
            lButton[i].setOnAction(ae->
            {
                  cPane.getChildren().clear();
                  cPane.getChildren().add(cP);
            });
      }

      // configure the buttons on the left block
      public GridPane lConfig()
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

            lSetButtons(0, cPane0); // -----> to lSetButtons(int, CenterPane)
            lSetButtons(1, cPane1);
            lSetButtons(2, cPane2);
            lSetButtons(3, cPane3);
            lSetButtons(4, cPane4);

            return lPane;
      }

      // check if the user input matches the answer
      public void check(int n)
      {
            cGuess[n] = new String(cTField[n].getText());
            if(cGuess[n].equals(cAns[n]))
            {
                  cTextLower[n].setText("yes :)");
                  lButton[n + 1].setVisible(true);
            }
            else
            {
                  cTextLower[n].setText("WRONGGGGGGG!!!!!");
            }
      }

      // setup an inner pane for the center block
      public CenterPane cPageSetup(CenterPane gPane, int i)
      {
            gPane.add(cButton[i], 0, 1);
            gPane.add(cTField[i], 0, 2);
            gPane.add(cTextLower[i], 0, 3);
            if(i < NUM - 1)
            {
                  cButton[i].setOnAction(ae->
                  {     
                        check(i); // -----> to check(int)
                  });
            }
            return gPane;
      }

      // configure the question pane
      public StackPane cConfig()
      {
            for(int b = 0; b < 5; b++)
            {
                  cAns[b] = new String("1" + b);
                  cButton[b] = new Button("cButton " + b);
                  cTField[b] = new TextField();
                  cTextLower[b] = new Text("This is pane " + b);
            }

            cPane0 = cPageSetup(cPane0, 0); // -----> to cPageSetup(GridPane, int)
            cPane1 = cPageSetup(cPane1, 1);
            cPane2 = cPageSetup(cPane2, 2);
            cPane3 = cPageSetup(cPane3, 3);
            cPane4 = cPageSetup(cPane4, 4);

            cPane.setStyle("-fx-background-color: #A4C3B2");
            cPane.getChildren().add(cPane0);
            StackPane.setAlignment(cPane0, Pos.CENTER);
            return cPane;
      }

      public void rConfig()
      {
            root.setStyle("-fx-alignment: center");
            root.setStyle("-fx-font: 30 Verdana");
            root.setTop(topPane);
            root.setBottom(bottomPane);
            root.setLeft(lPane);
            root.setCenter(cPane); 
      }

      public void tConfig()
      {
            topPane.getChildren().addAll(new Text("Welcome to the Game!"));
            topPane.setStyle("-fx-background-color: #6B9080");
            topPane.setPadding(new Insets(15, 15, 15, 15));
      }

      // configure the root pane
      public void bConfig()
      {
            bottomPane.setStyle("-fx-background-color: #EAF4F4");
            bottomPane.getChildren().addAll(new Text("(It is a game)"));
            bottomPane.setPadding(new Insets(15, 15, 15, 15));
      }
}
