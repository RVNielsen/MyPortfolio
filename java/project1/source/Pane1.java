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

import javafx.scene.input.MouseEvent;

public class Pane1
{
      // number of squares on the board
      private final int RNUM = 42;

      // an array of RNUM rectangles arranged as a board
      private Rectangle[] board = new Rectangle[RNUM];
      private final int[] BLACKSPACES = {7, 10, 12, 13, 16, 17, 18, 23, 24, 25, 28, 29, 31, 34};
      private final int[] WHITESPACES = {0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 14, 15, 19, 20, 21, 22, 
            26, 27, 30, 32, 33, 35, 36, 37, 38, 39, 40, 41};
      // number of whitespaces
      private final int WSNUM = 28;

      // is an indivdual square taken
      private boolean[] taken = new boolean[RNUM];
      // used for checking if all sqaures have been taken
      private boolean takenFlag;

      // clear all sqaures (besides sources)
      private Button clearButton = new Button("Clear");

      private int currentPlayer = 0;
      private final int PLAYERNUM = 6;
      // stores the square that the current player last clicked
      private int[] prevClick = new int[PLAYERNUM];
      
      // temporary rectangle for storing a color
      private Rectangle tempTangle = new Rectangle();

      // for placing the buttons on the pane
      private int x;
      private int y;
      // distance from previous space to the attempted next space
      private double checkDistance;

      // buttons for changing panes
      private Button leftButton = new Button();

      // used for setting the square sizes relative to the screen size
      GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
      private int rSize;

      // page 1 main function
      // horse game
      protected void pane1Main(CenterPane cP, Button lB)
      {
            setNotTaken();
            cP.add(clearButton, 0, 0);
            clearBoard();
            board = boardConfig(cP); // -----> to boardConfig(CenterPane)
            prevConfig(); // -----> to prevConfig()
            for(int p = 0; p < WSNUM - 6; p++)
            {
                  rClick(board[WHITESPACES[p]], WHITESPACES[p], lB); // -----> to rClick(Rectangle)
            }
            for(int y = 0; y < PLAYERNUM; y++)
            {
                  colorSquaresClick(y);
            }
      }

      // make all squares (besides source) white
      protected void clearBoard()
      {
            clearButton.setOnAction(ae->
            {
                  setNotTaken(); // -----> to setNotTaken()
                  prevConfig();
                  for(int g = 0; g < WSNUM - 6; g++)
                  {
                        board[WHITESPACES[g]].setFill(Color.WHITE);
                  }
            });
      }

      // mark all spaces as not clicked
      protected void setNotTaken()
      {
            for(int h = 0; h < WSNUM; h++)
            {
                  taken[WHITESPACES[h]] = false;
            }
            for(int g = RNUM - 6; g < RNUM; g++)
            {
                  taken[g] = true;
            }
      }

      // previous click for color c is square _
      protected void prevConfig()
      {
            for(int c = 0; c < PLAYERNUM; c++)
            {
                  prevClick[c] = RNUM - 6 + c;
            }
      }

      // is this click valid
      protected boolean isValidSpace(int e)
      {
            checkDistance = Math.pow((prevClick[currentPlayer] % 6 - e % 6), 2) + (Math.pow((prevClick[currentPlayer] / 6 - e / 6), 2));
            if(checkDistance == 5)
            {
                  return true;
            }
            return false;
      }

      // when initial row squares are clicked, change the player color
      protected void colorSquaresClick(int b)
      {
            switch(b)
            {
                  case 0:
                        board[b + RNUM - 6].setFill(Color.web("#3A2E39"));
                        break;
                  case 1:
                        board[b + RNUM - 6].setFill(Color.web("#8FC93A"));
                        break;
                  case 2:
                        board[b + RNUM - 6].setFill(Color.web("#0072BB"));
                        break;
                  case 3:
                        board[b + RNUM - 6].setFill(Color.web("#E4CC37"));
                        break;
                  case 4:
                        board[b + RNUM - 6].setFill(Color.web("#103900"));
                        break;
                  case 5:
                        board[b + RNUM - 6].setFill(Color.web("#E18335"));
                        break;
                  default:
                        board[b + RNUM - 6].setFill(Color.GRAY);
            }
            board[b + RNUM - 6].setOnMouseClicked(new EventHandler<MouseEvent>()
            {
                  @Override
                  public void handle(MouseEvent t)
                  {
                       currentPlayer = b;
                  }
            });
      }

      // set up the board
      protected Rectangle[] boardConfig(CenterPane cP)
      {
            rSize = gd.getDisplayMode().getWidth();
            rSize *= .05;
            Rectangle[] r = new Rectangle[RNUM];
            for(int u = 0; u < RNUM; u++)
            {
                  r[u] = new Rectangle(rSize, rSize);
                  // place all 0 - RNUM squares in a grid formation
                  x = u % 6 + 1;
                  y = u / 6 + 1;
                  r[u].setFill(Color.WHITE);
                  r[u].setStroke(Color.BLACK);
                  cP.add(r[u], x, y);
            }
            for(int b = 0; b < BLACKSPACES.length; b++)
            {
                  r[BLACKSPACES[b]].setFill(Color.BLACK);
            }
            return r;
      }

      // handle what happens when spaces are clicked
      protected void rClick(Rectangle a, int i, Button b)
      {
            a.setOnMouseClicked(new EventHandler<MouseEvent>()
            {
                  @Override
                  public void handle(MouseEvent t)
                  {
                        // if the space is free and the correct distance away
                        if(isValidSpace(i) && taken[i] == false)
                        {
                              // fill the space with the current player's color
                              switch(currentPlayer)
                              {
                                    case 0:
                                          a.setFill(Color.web("#3A2E39"));
                                          break;
                                    case 1:
                                          a.setFill(Color.web("#8FC93A"));
                                          break;
                                    case 2:
                                          a.setFill(Color.web("#0072BB"));
                                          break;
                                    case 3:
                                          a.setFill(Color.web("#E4CC37"));
                                          break;
                                    case 4:
                                          a.setFill(Color.web("#103900"));
                                          break;
                                    case 5:
                                          a.setFill(Color.web("#E18335"));
                                          break;
                                    default:
                                          a.setFill(Color.GRAY);
                              }
                              // set this space to the current player's previous click
                              prevClick[currentPlayer] = i;
                              // set this space as taken
                              taken[i] = true;
                              takenFlag = true;
                              // check if all spaces are taken
                              for(int h = 0; h < WSNUM; h++)
                              {
                                    if(taken[WHITESPACES[h]] == false)
                                    {
                                          takenFlag = false;
                                    }
                              }
                              // if all spaces are taken, the game is over
                              if(takenFlag == true)
                              {
                                    b.setVisible(true); // ***Button2 visible***
                              }
                        }
                        // if the click was not on a valid space
                        else
                        {
                              // get the color of the offending player
                              tempTangle.setFill(board[prevClick[currentPlayer]].getFill());
                              for(int k = 0; k < WSNUM - 6; k++)
                              {
                                    // if a square matches the offending player's color,
                                    //    set it to white and not taken
                                    if(tempTangle.getFill().equals(board[WHITESPACES[k]].getFill()))
                                    {
                                          board[WHITESPACES[k]].setFill(Color.WHITE);
                                          taken[WHITESPACES[k]] = false;
                                    }
                              }
                              // find the source of the current player and set it as the previous click
                              for(int w = RNUM - 6; w < RNUM; w++)
                              {
                                    if(tempTangle.getFill().equals(board[w].getFill()))
                                    {
                                          prevClick[currentPlayer] = w;
                                          break;
                                    }
                              }
                        }
                  }
            });
      }
}
