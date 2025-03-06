#include "helpers.h"
#include <math.h>

int getMin(int a, int b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    int red;
    int green;
    int blue;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get every color value
            red = image[i][j].rgbtRed;
            green = image[i][j].rgbtGreen;
            blue = image[i][j].rgbtBlue;

            // Calculate average
            average = round((red + green + blue) / 3.0);

            // Apply average value to every color
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Make temporary variable and calculate iterations (half of width pixels)
    RGBTRIPLE temp;
    int iterations = width / 2;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < iterations; j++)
        {
            // Replace j-th pixel with ending pixel minus j
            temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make copy array
    RGBTRIPLE copy[height][width];

    int new_i;
    int new_j;
    int copyRed;
    int copyGreen;
    int copyBlue;
    float count;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Reset values
            copyRed = 0;
            copyGreen = 0;
            copyBlue = 0;
            count = 0.0;

            // Make fixes k and l that applies to indexes
            for (int k = -1; k <= 1; k++)
            {
                // Make new i index
                new_i = i + k;

                // If pixel doesn't exist then ignore
                if (new_i < 0 || new_i >= height)
                {
                    continue;
                }

                // Same as above
                for (int l = -1; l <= 1; l++)
                {
                    new_j = j + l;
                    if (new_j < 0 || new_j >= width)
                    {
                        continue;
                    }

                    // Sum color values and add count
                    copyRed += image[new_i][new_j].rgbtRed;
                    copyGreen += image[new_i][new_j].rgbtGreen;
                    copyBlue += image[new_i][new_j].rgbtBlue;
                    count++;
                }
            }

            // Calculate average and round it
            copyRed = round(copyRed / count);
            copyGreen = round(copyGreen / count);
            copyBlue = round(copyBlue / count);

            // Apply every color to pixel in copy
            copy[i][j].rgbtRed = copyRed;
            copy[i][j].rgbtGreen = copyGreen;
            copy[i][j].rgbtBlue = copyBlue;
        }
    }

    // Replace original image with copy
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            image[h][w] = copy[h][w];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Make copy and make two arrays with Gx and Gy
    RGBTRIPLE copy[height][width];
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    int new_i;
    int new_j;
    int yInd;
    int xInd;

    int GxRed;
    int GxGreen;
    int GxBlue;

    int GyRed;
    int GyGreen;
    int GyBlue;

    // For every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Reset values
            GxRed = 0;
            GxGreen = 0;
            GxBlue = 0;
            GyRed = 0;
            GyGreen = 0;
            GyBlue = 0;

            // Make fixed index (k and l) to take pixels around the "parent pixel" with the parent pixel included
            for (int k = -1; k <= 1; k++)
            {
                // Fixed i and fixed y index
                new_i = i + k;
                yInd = k + 1;

                // If pixel doesn't exist then ignore it
                if (new_i < 0 || new_i >= height)
                {
                    continue;
                }

                for (int l = -1; l <= 1; l++)
                {
                    // Fixed j and x indexes
                    new_j = j + l;
                    xInd = l + 1;

                    // Ignore not existing indexes
                    if (new_j < 0 || new_j >= width)
                    {
                        continue;
                    }

                    // Multiply every color value by Gx and Gy value
                    GxRed += image[new_i][new_j].rgbtRed * Gx[yInd][xInd];
                    GyRed += image[new_i][new_j].rgbtRed * Gy[yInd][xInd];
                    GxGreen += image[new_i][new_j].rgbtGreen * Gx[yInd][xInd];
                    GyGreen += image[new_i][new_j].rgbtGreen * Gy[yInd][xInd];
                    GxBlue += image[new_i][new_j].rgbtBlue * Gx[yInd][xInd];
                    GyBlue += image[new_i][new_j].rgbtBlue * Gy[yInd][xInd];
                }
            }

            // Get color value by getting rounded square root from powered Gx + Gy values OR 255 if value is too high
            copy[i][j].rgbtRed = getMin(round(sqrt((GxRed * GxRed) + (GyRed * GyRed))), 255);
            copy[i][j].rgbtGreen = getMin(round(sqrt((GxGreen * GxGreen) + (GyGreen * GyGreen))), 255);
            copy[i][j].rgbtBlue = getMin(round(sqrt((GxBlue * GxBlue) + (GyBlue * GyBlue))), 255);
        }
    }

    // Replace original image by copy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}

// If a is lower than b then return a...else return b
int getMin(int a, int b)
{
    return (a < b) ? a : b;
}
