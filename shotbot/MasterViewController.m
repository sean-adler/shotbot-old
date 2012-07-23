//
//  MasterViewController.m
//  ShotBot
//
//  Created by Sean Adler on 7/20/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "MasterViewController.h"

#import "DetailViewController.h"

@implementation MasterViewController

@synthesize detailViewController = _detailViewController;
@synthesize drinkNames;

- (void)awakeFromNib
{
    self.clearsSelectionOnViewWillAppear = NO;
    self.contentSizeForViewInPopover = CGSizeMake(320.0, 600.0);
    [super awakeFromNib];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    // Deprecated method -- right now it only lists our drink names
    // Can either create drinks inside viewDidLoad or createDrinkProperties
    [self populateDrinkList];
    self.detailViewController = (DetailViewController *)[[self.splitViewController.viewControllers lastObject] topViewController];
    [self.tableView selectRowAtIndexPath:[NSIndexPath indexPathForRow:0 inSection:0] animated:NO scrollPosition:UITableViewScrollPositionMiddle];
    
}

- (void)viewDidUnload
{
    [self setDrinkNames:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (NSInteger)numberOfSectionsInTableView:(UITableView *)aTableView {
    // Return the number of sections.
    // We only have one section, with no section title.
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView 
 numberOfRowsInSection:(NSInteger)section
{
    return [drinkNames count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"Cell";
    
    UITableViewCell *cell = [tableView 
                             dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] 
                initWithStyle:UITableViewCellStyleDefault 
                reuseIdentifier:CellIdentifier];
    }
    
    // [self configureCell:cell atIndexPath:indexPath];
    
    cell.textLabel.text = [drinkNames objectAtIndex:indexPath.row];      
    return cell;
}

- (void)populateDrinkList {
    // Create the drink array which appears in the table
    self.drinkNames = [[NSArray alloc] initWithObjects:
                       @"Screwdriver", @"Tequila Sunrise", @"Whiskey Sour", nil];
    
}

- (void)tableView:(UITableView *)aTableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    // List cases for different drinks  (check string instead of object index for better readability)
    // Update ingredients appropriately.
    NSString *chosenDrink = [drinkNames objectAtIndex:indexPath.row];
    NSLog(@"%@", chosenDrink);
    
    if (chosenDrink == @"Screwdriver") {
        self.detailViewController.slider1.value = 0.0;
        self.detailViewController.slider2.value = 0.0;
        self.detailViewController.slider3.value = 0.8;
        self.detailViewController.slider4.value = 0.0;
        self.detailViewController.slider5.value = 0.8;
        self.detailViewController.slider6.value = 0.0;
        self.detailViewController.slider7.value = 0.0;
        self.detailViewController.slider8.value = 0.0;
    }
    else if (chosenDrink == @"Tequila Sunrise") {
        self.detailViewController.slider1.value = 0.0;
        self.detailViewController.slider2.value = 0.8;
        self.detailViewController.slider3.value = 0.0;
        self.detailViewController.slider4.value = 0.0;
        self.detailViewController.slider5.value = 0.4;
        self.detailViewController.slider6.value = 0.4;
        self.detailViewController.slider7.value = 0.0;
        self.detailViewController.slider8.value = 0.0;
    }
    else if (chosenDrink == @"Whiskey Sour") {
        self.detailViewController.slider1.value = 0.8;
        self.detailViewController.slider2.value = 0.0;
        self.detailViewController.slider3.value = 0.0;
        self.detailViewController.slider4.value = 0.0;
        self.detailViewController.slider5.value = 0.0;
        self.detailViewController.slider6.value = 0.0;
        self.detailViewController.slider7.value = 0.0;
        self.detailViewController.slider8.value = 0.8;
    }
    
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

/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/

/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath
{
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source.
        [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
    } else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view.
    }   
}
*/

/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath
{
}
*/

/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/

@end
