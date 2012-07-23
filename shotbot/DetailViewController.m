//
//  DetailViewController.m
//  ShotBot
//
//  Created by Sean Adler on 7/20/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "DetailViewController.h"

@interface DetailViewController ()
@property (strong, nonatomic) UIPopoverController *masterPopoverController;
- (void)configureView;
@end

@implementation DetailViewController

@synthesize sliderList;
@synthesize sliderLabelList;
@synthesize urlString;

@synthesize slider1, slider2, slider3, slider4, slider5, slider6, slider7, slider8;

@synthesize detailItem = _detailItem;
@synthesize detailDescriptionLabel = _detailDescriptionLabel;
@synthesize masterPopoverController = _masterPopoverController;

#pragma mark - Slider value methods

- (IBAction)pourDrink:(id)sender {
    // We expect the string to be 8 characters long
    NSMutableString *drinkString = [[NSMutableString alloc] init];
    // Append to address string the values from all sliders
    for (UISlider *slider in sliderList) {
        int drinkAmount = slider.value*10;
        [drinkString appendString:[NSString stringWithFormat:@"%d", drinkAmount]];
    }
    // Change practiceURL to the Flask server URL
    NSString *practiceURL = [NSString stringWithFormat:@"http://127.0.0.1:5000/%@", drinkString];
    NSURL *url = [NSURL URLWithString:practiceURL];
    NSURLRequest *urlRequest = [NSURLRequest requestWithURL:url];
    // Create connection -- request the fuckin URL!
    NSURLConnection *urlConnection = [NSURLConnection connectionWithRequest:urlRequest delegate:self];
    if (urlConnection) {
        NSLog(@"Connection made! Requesting %@", practiceURL);
    } else {
        NSLog(@"Connection never made ;(");
    }
}

#pragma mark - Managing the detail item

- (void)setDetailItem:(id)newDetailItem
{
    if (_detailItem != newDetailItem) {
        _detailItem = newDetailItem;
        
        // Update the view.
        [self configureView];
    }

    if (self.masterPopoverController != nil) {
        [self.masterPopoverController dismissPopoverAnimated:YES];
    }        
}

- (void)configureView
{
    // Update the user interface for the detail item.
    if (self.detailItem) {
        self.detailDescriptionLabel.text = [self.detailItem description];
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    // Store all sliders in a list
    sliderList = [[NSMutableArray alloc] init];
    [sliderList addObject:slider1];
    [sliderList addObject:slider2];
    [sliderList addObject:slider3];
    [sliderList addObject:slider4];
    [sliderList addObject:slider5];
    [sliderList addObject:slider6];
    [sliderList addObject:slider7];
    [sliderList addObject:slider8];
    
    // Set all values to 0.0 (to match slider starting position)
    for (UILabel *sliderLabel in sliderLabelList) {
        sliderLabel.text = [NSString stringWithFormat:@"0.0"];
    }
    
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    [self configureView];
}

- (void)viewDidUnload
{
    pourDrinkButton = nil;
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
}

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
}

- (void)viewWillDisappear:(BOOL)animated
{
	[super viewWillDisappear:animated];
}

- (void)viewDidDisappear:(BOOL)animated
{
	[super viewDidDisappear:animated];
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return YES;
}

#pragma mark - Split view

- (void)splitViewController:(UISplitViewController *)splitController willHideViewController:(UIViewController *)viewController withBarButtonItem:(UIBarButtonItem *)barButtonItem forPopoverController:(UIPopoverController *)popoverController
{
    barButtonItem.title = NSLocalizedString(@"Master", @"Master");
    [self.navigationItem setLeftBarButtonItem:barButtonItem animated:YES];
    self.masterPopoverController = popoverController;
}

- (void)splitViewController:(UISplitViewController *)splitController willShowViewController:(UIViewController *)viewController invalidatingBarButtonItem:(UIBarButtonItem *)barButtonItem
{
    // Called when the view is shown again in the split view, invalidating the button and popover controller.
    [self.navigationItem setLeftBarButtonItem:nil animated:YES];
    self.masterPopoverController = nil;
}

@end
