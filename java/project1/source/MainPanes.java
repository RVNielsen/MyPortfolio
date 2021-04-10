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

import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;

import code.CenterPane;

public class MainPanes extends Application
{
      // number of pages
      final int PAGENUM = 5;

      // root pane
      BorderPane root = new BorderPane();
      // title pane
      StackPane topPane = new StackPane();
      // lower pane
      StackPane bottomPane = new StackPane();
      
      // buttons to control page switching
      Button[] lButton = new Button[PAGENUM];
      GridPane lPane = new GridPane();
      
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

            cPane0.which(cPane0, 0, lButton[1]); // -----> to which(CenterPane, int)
            cPane0.which(cPane1, 1, lButton[2]);
            cPane0.which(cPane2, 2, lButton[3]);
            cPane0.which(cPane3, 3, lButton[4]);
            cPane0.which(cPane4, 4, lButton[0]);

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

      // configure the root pane
      public void rConfig()
      {
            root.setStyle("-fx-alignment: center");
            root.setStyle("-fx-font: 30 Verdana");
            root.setTop(topPane);
            root.setBottom(bottomPane);
            root.setLeft(lPane);
            root.setCenter(cPane); 
      }
      
      // configure the buttons on the left block
      public GridPane lConfig()
      {
            lPane.setStyle("-fx-background-color: #CCE3DE");
            for(int a = 0; a < PAGENUM; a++)
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
      
      // set up the left side buttons
      public void lSetButtons(int i, CenterPane cP)
      {
            lButton[i].setOnAction(ae->
            {
                  cPane.getChildren().clear();
                  cPane.getChildren().add(cP);
            });
      }

      // configure the question pane
      public StackPane cConfig()
      {
            cPane.getChildren().add(cPane0);
            cPane.setStyle("-fx-background-color: #A4C3B2");
            cPane.setAlignment(cPane0, Pos.CENTER);
            return cPane;
      }

      // configure the header pane
      public void tConfig()
      {
            topPane.getChildren().addAll(new Text("Welcome to the Game!"));
            topPane.setStyle("-fx-background-color: #6B9080");
            topPane.setPadding(new Insets(15, 15, 15, 15));
      }

      // configure the footer pane
      public void bConfig()
      {
            bottomPane.getChildren().addAll(new Text("(It is a game)"));
            bottomPane.setStyle("-fx-background-color: #EAF4F4");
            bottomPane.setPadding(new Insets(15, 15, 15, 15));
      }

      public static void main(String[] args) 
      {        
            launch(args);    
      }

}
