import axios from 'axios';

export const getIndexes = async () => {
  const response = await axios.get('/api/indexes');
  return response.data;
};

export const getRegionIndexes = async () => {
  const response = await axios.get('/api/regions');
  return response.data;
};