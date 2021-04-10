package code;

import javafx.application.Application;
import javafx.scene.layout.GridPane;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.event.EventHandler;
import javafx.scene.text.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;
import java.util.Scanner;
import javafx.scene.control.Button;

import javafx.scene.input.MouseEvent;

public class Pane1
{
      // number of rectangles on the board
      private final int RNUM = 42;
      private final int[] BLACKSPACES = {7, 10, 12, 13, 16, 17, 18, 23, 24, 25, 28, 29, 31, 34};
      private final int[] WHITESPACES = {0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 14, 15, 19, 20, 21, 22, 
            26, 27, 30, 32, 33, 35, 36, 37, 38, 39, 40, 41};
      private final int WSNUM = 28;

      private boolean[] taken = new boolean[RNUM];
      private Rectangle tempTangle = new Rectangle();

      // number of players
      private final int PLAYERNUM = 6;
      private final int DISTANCE = 5;

      private Button clearButton = new Button("Clear");
      private Rectangle[] board = new Rectangle[RNUM];

      // for placing the buttons on the pane
      private int x;
      private int y;
      private int currentPlayer = 0;
      private int[] prevClick = new int[PLAYERNUM];

      private double checkDistance;
      private boolean takenFlag;
      private Button leftButton = new Button();

      // page 1 main function
      // board
      protected String pane1Main(CenterPane cP, Button lB)
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
            return "Green";
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

      // previous click for color c is rectangle _
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
            if(checkDistance == DISTANCE)
            {
                  return true;
            }
            return false;
      }

      // when initial row rectangles are clicked, change the player color
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
            Rectangle[] r = new Rectangle[RNUM];
            for(int u = 0; u < RNUM; u++)
            {
                  r[u] = new Rectangle(50, 50);
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
                        System.out.println("currentPlayer is: " + currentPlayer);
                        System.out.println("prevClick[currentPlayer] is: " + prevClick[currentPlayer]);
                        if(isValidSpace(i) && taken[i] == false)
                        {
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
                              prevClick[currentPlayer] = i;
                              System.out.println("prev click is now " + prevClick[currentPlayer]);
                              taken[i] = true;
                              takenFlag = true;
                              for(int h = 0; h < WSNUM; h++)
                              {
                                    if(taken[WHITESPACES[h]] == false)
                                    {
                                          takenFlag = false;
                                    }
                              }
                              if(takenFlag == true)
                              {
                                    b.setVisible(true); // ***Button2 visible***
                              }
                        }
                        else
                        {
                              tempTangle.setFill(board[prevClick[currentPlayer]].getFill());
                              // for all spaces
                              for(int k = 0; k < WSNUM; k++)
                              {
                                    if(board[WHITESPACES[k]].getFill() != Color.WHITE)
                                    {
                                          // if the offending space has the same color as the previous space
                                          if(board[WHITESPACES[k]].getFill() == tempTangle.getFill())
                                          {
                                                if(k < WSNUM - 6)
                                                {
                                                      board[WHITESPACES[k]].setFill(Color.WHITE);
                                                }
                                                else
                                                {
                                                      prevClick[currentPlayer] = WHITESPACES[k];
                                                      break;
                                                }
                                          }
                                    }
                              }
                        }
                  }
            });
      }
}
