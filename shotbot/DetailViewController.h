//
//  DetailViewController.h
//  ShotBot
//
//  Created by Sean Adler on 7/20/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController <UISplitViewControllerDelegate> {
    
    NSMutableData *receivedData;
    
    IBOutlet UIButton *pourDrinkButton;
    
    IBOutlet UISlider *slider1;
    
    IBOutlet UISlider *slider2;
    
    IBOutlet UISlider *slider3;
    
    IBOutlet UISlider *slider4;
    
    IBOutlet UISlider *slider5;
    
    IBOutlet UISlider *slider6;
    
    IBOutlet UISlider *slider7;
    
    IBOutlet UISlider *slider8;
    
}

@property (nonatomic, retain) NSMutableArray *sliderList;
@property (nonatomic, retain) NSMutableArray *sliderLabelList;
@property (nonatomic, retain) NSString *urlString;

@property (nonatomic, retain) IBOutlet UISlider *slider1;

@property (nonatomic, retain) IBOutlet UISlider *slider2;

@property (nonatomic, retain) IBOutlet UISlider *slider3;

@property (nonatomic, retain) IBOutlet UISlider *slider4;

@property (nonatomic, retain) IBOutlet UISlider *slider5;

@property (nonatomic, retain) IBOutlet UISlider *slider6;

@property (nonatomic, retain) IBOutlet UISlider *slider7;

@property (nonatomic, retain) IBOutlet UISlider *slider8;



@property (strong, nonatomic) id detailItem;

@property (strong, nonatomic) IBOutlet UILabel *detailDescriptionLabel;

@end
