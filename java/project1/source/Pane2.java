package code;

import javafx.application.Application;
import javafx.scene.layout.GridPane;
import javafx.scene.Scene;
import javafx.event.EventHandler;
import javafx.scene.text.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;
import java.util.Scanner;
import javafx.scene.control.Button;

import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;
import javafx.scene.shape.Shape;

import javafx.scene.input.MouseEvent;
import java.io.File;

import javafx.scene.shape.Path;
import javafx.scene.shape.Polyline;
import javafx.scene.shape.Line;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;

public class Pane2
{
      private int rWidth;
      private int rHeight;
      private final int RNUM = 35;
      private int x;
      private int y;

      private Image i;
      private ImagePattern ip;

      private boolean draw = true;
      private boolean notDone = true;
      private boolean first = true;

      private Line line = new Line();

      private Rectangle[] board = new Rectangle[RNUM];
      GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();

      protected void pane2Main(CenterPane cP, Button lB)
      {
            board = boardConfig(cP);
            getPics();
            drawLine(cP);
      }

      protected void getPics()
      {
            for(int h = 0; h < RNUM; h++)
            {
                  i = new Image("/calendar/s" + h + ".png");
                  ip = new ImagePattern(i);
                  board[h].setFill(ip);
            }
      }

      // set up the board
      protected Rectangle[] boardConfig(CenterPane cP)
      {
            rWidth = gd.getDisplayMode().getWidth();
            rWidth *= .08;
            Rectangle[] r = new Rectangle[RNUM];
            for(int u = 0; u < RNUM; u++)
            {
                  r[u] = new Rectangle(rWidth, rWidth);
                  // place all 0 - RNUM squares in a grid formation
                  x = u % 7;
                  y = u / 7;
                  r[u].setFill(Color.WHITE);
                  r[u].setStroke(Color.BLACK);
                  cP.add(r[u], x, y);
            }
            return r;
      }

      protected drawLine(CenterPane cP)
      {
            line.setStartX(100);
            line.setStartY(100);
            line.setEndX(200);
            line.setEndY(200);
            line.setStrokeWidth(2);
            line.setStroke(Color.BLUE);
            
            cP.getChildren().add(line);
      }
}