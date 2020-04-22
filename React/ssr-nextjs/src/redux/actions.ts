import { SampleReactTypes } from './types';
import { action } from 'typesafe-actions';

export const sampleReactAction = () => action(SampleReactTypes.SAMEPLE_REACT_TYPE);

export const sampleReactActionAsync = () => action(SampleReactTypes.SAMEPLE_REACT_TYPE_ASYNC);
