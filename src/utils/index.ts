export function formatText(value: string) {
  return value.trim();
}

export function getShortText(value: string, maxLength = 100) {
  return value.length <= maxLength ? value : `${value.slice(0, maxLength)}...`;
}
