#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  uniqueArgs.sort((a, b) => b - a); // Sort in descending order
  console.log(uniqueArgs[1] || 0); // Second biggest, or 0 if not found
}
