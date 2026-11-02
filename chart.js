const     const height = canvas.height = canvas.parentElement.clientHeight || 200;
    ctx.clearRect(0, 0, width, height);
    if (!points || points.length < 2) return;
    const padding = 20;
    const chartW = width - padding * 2;
    const chartH = height - padding * 2;
    const maxVal = Math.max(...points, 5);
    // Grid lines
    ctx.strokeStyle = 'rgba(39, 53, 79, 0.4)';
    ctx.lineWidth = 1;
    for (let i = 0; i < 4; i++) {
      const y = padding + (chartH / 3) * i;
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(width - padding, y);
      ctx.stroke();
    }
    // Path
    ctx.beginPath();
    const stepX = chartW / (points.length - 1);
    points.forEach((val, idx) => {
      const x = padding + idx * stepX;
      const y = height - padding - (val / maxVal) * chartH;
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2.5;
    ctx.shadowColor = '#06b6d4';
    ctx.shadowBlur = 8;
    ctx.stroke();
    ctx.shadowBlur = 0;
    // Gradient fill under curve
    ctx.lineTo(width - padding, height - padding);
    ctx.lineTo(padding, height - padding);
    ctx.closePath();
    const grad = ctx.createLinearGradient(0, padding, 0, height - padding);
    grad.addColorStop(0, 'rgba(6, 182, 212, 0.35)');
    grad.addColorStop(1, 'rgba(6, 182, 212, 0.0)');
    ctx.fillStyle = grad;
    ctx.fill();
  }
};
window.CyberCharts = CyberCharts;