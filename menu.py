import pygame
import os
menu_image = pygame.transform.scale(pygame.image.load("images/upgrade_menu.png"), (200, 200))
upgrade_image = pygame.transform.scale(pygame.image.load("images/upgrade.png"), (70, 30))
sell_image = pygame.transform.scale(pygame.image.load("images/sell.png"), (40, 40))


class UpgradeMenu:
    def __init__(self, x, y):
        #self.x = x
        #self.y = y
        self.menu = menu_image
        self.upgrade = upgrade_image
        self.sell = sell_image
        self.rect = self.menu.get_rect()
        self.rect.center = (x, y)
        self.__buttons = [Button(upgrade_image, "upgrade", self.rect.centerx, self.rect.centery - 75), Button(sell_image, "sell", self.rect.centerx, self.rect.centery + 75) ]  # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu, self.rect)
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.__buttons[0].image, (self.rect.x + 65, self.rect.y + 15))
        win.blit(self.__buttons[1].image, (self.rect.x + 80, self.rect.y + 155))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons      #回傳list中的 button object
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()   #取得按鈕大小範圍
        self.rect.center = (x, y)           #取得按鈕中心座標
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return self.rect.collidepoint(x, y)   #如果有點擊到回傳True

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name                      #將按鈕的名稱回傳，以判斷是按哪個按鈕
