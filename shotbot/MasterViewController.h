//
//  MasterViewController.h
//  ShotBot
//
//  Created by Sean Adler on 7/20/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class DetailViewController;

@interface MasterViewController : UITableViewController

@property (strong, nonatomic) DetailViewController *detailViewController;
@property (strong, nonatomic) NSArray *drinkNames;

- (void)populateDrinkList;

@end
