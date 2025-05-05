window.onload = () => {
  // Smooth scroll to sections
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Tab switching for experiments
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.experiment-tab-content');

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(tab => tab.classList.remove('active', 'fade-in'));

      button.classList.add('active');
      const tab = button.getAttribute('data-tab');
      const target = document.getElementById(tab);
      if (target) {
        target.classList.add('active', 'fade-in');
      }
    });
  });

  // Add fade-in animation for tabs
  const fadeStyle = document.createElement('style');
  fadeStyle.textContent = `
    .fade-in {
      animation: fadeInTab 0.4s ease-in-out;
    }
    @keyframes fadeInTab {
      from {
        opacity: 0;
        transform: translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  `;
  document.head.appendChild(fadeStyle);

  // Chart setup
  const chartCanvas = document.getElementById('accuracyChart');
  if (chartCanvas) {
    const ctx = chartCanvas.getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          'Small: G+B+Color', 'Small: G+B+Rot', 'Small: SD V2',
          '5x: G+B', '5x: G+B+SD', '10x: Google', '10x: SD 3'
        ],
        datasets: [
          {
            label: 'Scratch Accuracy (%)',
            data: [14.07, 10.0, 15.5, 39.1, 30.8, 45.85, 31.5],
            backgroundColor: '#aecbe6'
          },
          {
            label: 'KD Accuracy (%)',
            data: [61.5, 35.4, 14.0, 38.1, 36.19, 70.6, 32.9],
            backgroundColor: '#005A8B'
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'top' }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 80,
            title: {
              display: true,
              text: 'Accuracy (%)'
            }
          }
        }
      }
    });
  }

  // Tag click-to-expand
  const tags = document.querySelectorAll('.tag.clickable');
  console.log("Tags found: " + tags.length);
  tags.forEach(tag => {
    tag.addEventListener('click', () => {
      const parent = tag.closest('.prompt-block');
      const outputBox = parent.querySelector('.click-info');
      const info = tag.getAttribute('data-info');

      if (outputBox.textContent === info && outputBox.style.display === 'block') {
        outputBox.style.display = 'none';
        outputBox.textContent = '';
      } else {
        outputBox.textContent = info;
        outputBox.style.display = 'block';
      }
    });
  });
};
