import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const InteractiveBudgetChart = ({ investmentData }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    if (investmentData && chartRef.current) {
      const svg = d3.select(chartRef.current);
      svg.selectAll('*').remove();

      const width = +svg.attr('width');
      const height = +svg.attr('height');
      const radius = Math.min(width, height) / 2;

      const color = d3.scaleOrdinal(d3.schemeCategory10);

      const pie = d3.pie()
        .value(d => d.value)
        .sort(null);

      const path = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

      const label = d3.arc()
        .outerRadius(radius - 40)
        .innerRadius(radius - 40);

      const g = svg.append('g')
        .attr('transform', `translate(${width / 2},${height / 2})`);

      const arc = g.selectAll('.arc')
        .data(pie(investmentData))
        .enter().append('g')
        .attr('class', 'arc');

      arc.append('path')
        .attr('d', path)
        .attr('fill', d => color(d.data.label));

      arc.append('text')
        .attr('transform', d => `translate(${label.centroid(d)})`)
        .attr('dy', '0.35em')
        .text(d => d.data.label);
    }
  }, [investmentData]);

  return (
    <svg ref={chartRef} width="960" height="500" />
  );
};

export default InteractiveBudgetChart;