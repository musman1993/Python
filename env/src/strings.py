
    # Draw current shape
    for row in range(len(current_shape)):
        for col in range(len(current_shape[0])):
            if current_shape[row][col]:
                pygame.draw.rect(screen, current_color, (current_x + col * CELL_SIZE, current_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit pygame
pygame.quit()