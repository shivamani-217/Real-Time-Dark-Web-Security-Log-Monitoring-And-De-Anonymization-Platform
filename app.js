doc            severity,
            raw_content: content,
            threat_actor: actor || 'UNKNOWN_ACTOR',
            risk_score: severity === 'CRITICAL' ? 95 : (severity === 'HIGH' ? 82 : 60)
          })
        });
        if (res.ok) {
          document.getElementById('ingestModal').classList.remove('open');
          document.getElementById('customLogContent').value = '';
          this.showToast('Custom security log ingested successfully', 'normal');
        }
      } catch (err) {
        console.error('Failed to ingest log', err);
      }
    },
    // --- UTILITIES ---
    showToast(message, type = 'normal') {
      const container = document.getElementById('toastContainer');
      if (!container) return;
      const toast = document.createElement('div');
      toast.className = `toast ${type === 'alert' ? 'toast-alert' : ''}`;
      toast.innerHTML = `
        <span style="font-size: 1.1rem;">${type === 'alert' ? '🚨' : '⚡'}</span>
        <div style="flex: 1; font-weight: 600;">${this.escapeHtml(message)}</div>
      `;
      container.appendChild(toast);
      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(() => toast.remove(), 300);
      }, 4500);
    },
    escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }
  };
  window.App = App;
  App.init();
});