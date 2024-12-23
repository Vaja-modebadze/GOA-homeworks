let productMap = new Map();
productMap.set('name', 'Laptop');
productMap.set('price', 1200);
productMap.set('brand', 'Dell');

console.log('Map before clear:', productMap);
productMap.clear();

if (productMap.size === 0) {
  console.log('The map is now empty.');
} else {
  console.log('The map still has data.');
}