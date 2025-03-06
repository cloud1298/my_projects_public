#include "helpers.h"
#include <math.h>

int getMin(int a, int b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Make average value and apply it to every RGB value
            average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;

    int realRed;
    int realGreen;
    int realBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            sepiaRed = round((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue));
            realRed = getMin(sepiaRed, 255);

            sepiaGreen = round((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue));
            realGreen = getMin(sepiaGreen, 255);

            sepiaBlue = round((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue));
            realBlue = getMin(sepiaBlue, 255);

            image[i][j].rgbtRed = realRed;
            image[i][j].rgbtGreen = realGreen;
            image[i][j].rgbtBlue = realBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Set ammount of swaps
    int swap_ammount = width / 2;

    // For every pixel until in the middle - swap j pixel with the pixel at the end minus j
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < swap_ammount; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Space for image copy
    RGBTRIPLE copy[height][width];

    int sumRed;
    int sumGreen;
    int sumBlue;
    float count;

    int sum_i;
    int sum_j;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Reset values
            sumRed = 0;
            sumGreen = 0;
            sumBlue = 0;
            count = 0.0;

            // Make new indexes (sum_i and sum_j) by adding fix to old indexes
            for (int k = -1; k <= 1; k++)
            {
                sum_i = i + k;

                // If value is not reachable, then skip
                if (sum_i < 0 || sum_i >= height)
                {
                    continue;
                }

                for (int l = -1; l <= 1; l++)
                {
                    sum_j = j + l;

                    if (sum_j < 0 || sum_j >= width)
                    {
                        continue;
                    }

                    // Add colors value to sum and add count
                    sumRed += image[sum_i][sum_j].rgbtRed;
                    sumGreen += image[sum_i][sum_j].rgbtGreen;
                    sumBlue += image[sum_i][sum_j].rgbtBlue;
                    count++;
                }
            }

            // Calculate average of colors
            sumRed = round(sumRed / count);
            sumGreen = round(sumGreen / count);
            sumBlue = round(sumBlue / count);

            // Fill copy of image one by one pixel
            copy[i][j].rgbtRed = sumRed;
            copy[i][j].rgbtGreen = sumGreen;
            copy[i][j].rgbtBlue = sumBlue;
        }
    }

    // Replace image with copy
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image[h][w] = copy[h][w];
        }
    }

    return;
}

int getMin(int a, int b)
{
    return (a < b) ? a : b;
}
