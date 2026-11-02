class         this.lastMousePos = { x: screenX, y: screenY };
      } else {
        this.hoveredNode = this.getNodeAt(world.x, world.y);
        this.canvas.style.cursor = this.hoveredNode ? 'pointer' : 'grab';
      }
    });
    window.addEventListener('mouseup', () => {
      this.draggedNode = null;
      this.isPanning = false;
    });
    this.canvas.addEventListener('wheel', e => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      this.zoom(zoomFactor, e.clientX, e.clientY);
    });
  }
  zoom(factor, clientX, clientY) {
    const rect = this.canvas.getBoundingClientRect();
    const mouseX = clientX ? clientX - rect.left : this.canvas.width / 2;
    const mouseY = clientY ? clientY - rect.top : this.canvas.height / 2;
    const newScale = Math.min(Math.max(this.scale * factor, 0.4), 3.0);
    this.panX = mouseX - (mouseX - this.panX) * (newScale / this.scale);
    this.panY = mouseY - (mouseY - this.panY) * (newScale / this.scale);
    this.scale = newScale;
  }
  zoomIn() {
    this.zoom(1.2);
  }
  zoomOut() {
    this.zoom(0.8);
  }
  resetView() {
    this.scale = 1.0;
    this.panX = 0;
    this.panY = 0;
  }
}
window.AttributionGraph = AttributionGraph;